===================================
Lacework Python SDK Troubleshooting
===================================

This SDK uses standard python logging facilities. To turn on all of the debug information
use the following:

..  code-block::
    :caption: Turn on Debugging

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True