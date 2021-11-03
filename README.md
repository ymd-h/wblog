# Well-Bahaved Logging (wblog)

## Overview

Python standard `logging` package has great functionalities, however,
it is bit confusing.

For small one-time script, it is fine to use root logger functions
(e.g. `logging.debug()`) with global config `logging.basicConfig()`.
Moreover you don't need to call `logging.basicConfig()` explicitly
because `logging.debug()` etc. internally call it
to ensure the root logger has a handler.


For importable library, the situation is completely different. It is
officially recommended that loggers should not have any handlers
except `logging.NullHandler`. Logging should be configurable by end
users through top level main script or application.


Here, we provide a set of small utility functions to help library
developpers realize well-behaved logging.


## Install

```bash
pip install wblog
```

## Usage

### Get Logger at module
You can get module-level prepared `logging.Logger` instance by
`wblog.getLogger()` function. The function automatically detects the
module name (aka. `__name__`), so that you don't need to pass it.

```python
import wblog

logger = wblog.getLogger() # No __name__ is needed
```

The returned logger is standard `logging.Logger`, so that you can call
logging methods (e.g. `Logger.debug()`) as usual.


Since the logger is standart `logging.Logger`, it is also possible to
set log level and to add handlers manually, however, it is not
recommended.


### Start Logging
`wblog.start_logging(name, level=None, *, handlers=None, propagate=False)`
function enables logging of a specified package or module
(as long as they are well behaved).

If no handlers are passed, `logging.StreamHandler` is used and log
messages are printed out at console `sys.stderr`.

If `propagate=Flase` (default), the module stops delegation to parent
logger.

We assume the module logger doesn't have any handlers except `logging.NullLogger`,
and the function doesn't remove handlers.


### Stop Logging
`wblog.stop_logging(name)` function disables logging of a specified
package or module. It removes its log level and all handlers from `name`,
and enables delegation to the parent logger again.


## Design

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
(`logging.NOTSET`), removes all handlers, and enable delegation again.
