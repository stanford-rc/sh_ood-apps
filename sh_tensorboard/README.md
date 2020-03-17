## `sh_ondemand`

This [Tensorboard](https://www.tensorflow.org/tensorboard) OnDemand app runs through an authenticating reverse proxy. 

Tensorboard doesn't provide any kind of authentication for its web interface, so on a shared environment, anybody 
knowing the hostname and port number of a running Tensorboard instance can connect to it.

To mitigate this, we implemented an authentication mechanism that basically sets a browser cookie in the OnDemand 
interactive app page (through the "Connect to Tensorboard" button), which is then checked by the authenticating 
reverse proxy to control access to the Tensorboard web interface. 

Without that cookie, access to the Tensorboard 
web interface is refused. And if the cookie is ever lost, users can re-create it by visiting the 
"My Interactive Sessions" page and clicking the "Connect" button again.
