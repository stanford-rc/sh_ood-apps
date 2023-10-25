# Open OnDemand apps for Sherlock

This repository contains [Open OnDemand](https://openondemand.org/) used on
[Sherlock](https://www.sherlock.stanford.edu)

## `sh_codeserver`

Local customizations for [code-server](https://coder.com/docs/code-server), based on 
https://github.com/OSC/bc_osc_codeserver

## `sh_jupyter`

Local customizations for [Jupyter](https://jupyter.org/) notebooks, based on
https://github.com/OSC/bc_osc_jupyter

## `sh_rstudio`

Local customizations for [RStudio
Server](https://rstudio.com/products/rstudio/), based on
https://github.com/OSC/bc_osc_rstudio_server

## `sh_tensorboard`

OnDemand app for [Tensorboard](https://www.tensorflow.org/tensorboard)

Because Tensorboard doesn't provide any kind of authentication mechanism, this
app adds an transparent authentication layer, via an authenticating reverse
proxy and session cookies. The workflow is transparent for users, but
Tensorboard sessions can only be accessed through the OnDemand portal. 

