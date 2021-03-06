# Well-Bahaved Logging (wblog)

## 1. Overview

Python standard `logging` package has great functionalities, however,
it is bit confusing.

For small one-time script, it is fine to use root logger functions
(e.g. `logging.debug()`) with global config `logging.basicConfig()`.
Moreover you don't need to call `logging.basicConfig()` explicitly
because `logging.debug()` etc. internally call it
to ensure the root logger has a handler.


For importable library, the situation is completely different. It is
officially recommended that loggers should not have any handlers
except `logging.NullHandler`. Additionally, in our opinion, logging
should be configurable by end users through top level main script or
application.


Here, we provide a set of small utility functions to help library
developpers realize well-behaved logging.


## 2. Install
wblog doesn't have any dependencies.


```bash
pip install well-behaved-logging
```

## 3. Usage

### 3.1 Get and Use Logger at Module
You can get module-level prepared `logging.Logger` instance by
`wblog.getLogger()` function. The function automatically detects the
module name (aka. `__name__`), so that you don't need to pass it.


The returned logger is standard `logging.Logger`, so that you can call
logging methods (e.g. `Logger.debug()`) as usual.


```python
import wblog

logger = wblog.getLogger() # No __name__ is needed

logger.debug("Debug message")
```

Since the logger is standart `logging.Logger`, it is also possible to
set log level and to add handlers manually, however, it is not
recommended.


### 3.2 Start Logging (by End Users or Application)
`wblog.start_logging(name, level=None, *, handlers=None, propagate=False)`
function enables logging of a specified package or module
(as long as they are well behaved).

If no handlers are passed, `logging.StreamHandler` is used and log
messages are printed out at console `sys.stderr`.

If `propagate=Flase` (default), the module stops delegation to parent
logger.

We assume the module logger doesn't have any handlers except `logging.NullLogger`,
and the function doesn't remove handlers.


### 3.3 Stop Logging (by End Users or Application)
`wblog.stop_logging(name)` function disables logging of a specified
package or module. It removes its log level and all handlers from `name`,
and enables delegation to the parent logger again.


### 3.4 Advanced Usage
wblog doesn't manage handlers and fomatters.
End users or application need to prepare them.

Handler defines how and where the logging messages are outputted.
There are many handlers are implemented at the `logging` packages
([ref1](https://docs.python.org/3/library/logging.handlers.html),
[ref2](https://docs.python.org/3/howto/logging.html#useful-handlers)).

- `StreamHandler` writes logs to stream (e.g. srandard error).
- `FileHandler` writes logs to a file.
- `RotatingFileHandler` writes logs to a file with log rotation.
- etc.


`logging.Handler` class can set log level and filter, so that it is
also possible that all logs are shown on the console standard error
and only logs over `logging.WARNING` are written on the log file.

If you set only a single handler to your logger, we recommend not to
specify log level at the handler, then the handler manages all logs
from the logger.


Formatter defines logging format
([ref](https://docs.python.org/3/library/logging.html#formatter-objects))
and is set to handlers.

The default format is `%(levelname)s:%(name)s:%(message)s` which
doesn't include date time information at all.

Information can be used are described
[here](https://docs.python.org/3/library/logging.html#logrecord-attributes).


## 4. Design

```
root logger <-- package top-level logger <-- ... <-- module logger
```

We set `logging.NullHandler` to the package top-level logger.


When users change root logger config by `logging.basicConfig()`,
other (unconfigured) loggers should follow.


If users want to enable only a certain package or module, we should
set log level and handlers to that level logger. Generally, delegation
to its parent logger can be stopped, but it is better if it is
configurable.

Disabling such logging reverts to the original log level
(`logging.NOTSET`), removes all handlers, and enables delegation again.


## 5. Other Logging Libraries

There are many logging libraries. As far as we know, they are designed
for end users to log easily.

- [logzero](https://github.com/metachris/logzero)
  - Easy to setup `Logger`, `Handler`, and `Formatter`
	- Built on the standard `logging` package
  - For end users or application, not for library
- [Loguru](https://github.com/Delgan/loguru)
  - Easy to logging
	- Built from scratch
  - For end users or application, not for library
