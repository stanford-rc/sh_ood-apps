# Wait for the Tensorboard server to start
echo "Waiting for Tensorboard server to open port ${port}..."
echo "TIMING - Starting wait at: $(date)"
if wait_until_port_used "${node}:${port}" 60; then
  echo "Discovered Tensorboard server listening on port ${port}!"
  echo "TIMING - Wait ended at: $(date)"
else
  echo "Timed out waiting for Tensorboard server to open port ${port}!"
  echo "TIMING - Wait ended at: $(date)"
  pkill -P ${SCRIPT_PID}
  clean_up 1
fi
sleep 2
