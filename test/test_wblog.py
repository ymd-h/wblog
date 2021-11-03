import logging
import unittest

import wblog

import submodule


class TestWellBehavedLogging(unittest.TestCase):
    def test_wblog(self):
        """
        Test for wblog

        Since logger is global singleton, several tests are executed sequentially.
        """
        # Logger Creation
        logger = wblog.getLogger()

        ## Logger instance must be same with logging.getLogger(__name__).
        self.assertEqual(logger, logging.getLogger(__name__))

        ## Logger must have effective handler.
        self.assertTrue(logger.hasHandlers())


        # Start Logging
        level = logging.INFO
        handler = logging.StreamHandler()
        wblog.start_logging(__name__, level, handlers = handler)

        ## Logger level must be same with specified level.
        self.assertEqual(logger.level, level)

        ## Logger must has specified handler.
        self.assertIn(handler, logger.handlers)

        ## Logger propagation is disabled.
        self.assertFalse(logger.propagate)


        # Stop Logging
        wblog.stop_logging(__name__)

        ## Logger level must be NOTSET.
        self.assertEqual(logger.level, logging.NOTSET)

        ## Logger must not have specified handler, but has any effective handlers.
        self.assertNotIn(handler, logger.handlers)
        self.assertTrue(logger.hasHandlers())

        ## Logger propagation is enabled.
        self.assertTrue(logger.propagate)

    def test_module(self):
        """
        Test using submodule
        """
        # Logger creation
        logger = submodule.getLogger()

        ## Logger is different with current level logger
        self.assertNotEqual(logger, logging.getLogger(__name__))


if __name__ == "__main__":
    unittest.main()
