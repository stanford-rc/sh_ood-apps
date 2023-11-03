# Wait for server to start
echo "Waiting for server to open port ${port}..."
if wait_until_port_used "${host}:${port}" 60; then
  echo "Discovered server listening on port ${port}!"
else
  echo "Timed out waiting for server to open port ${port}!"
  pkill -P ${SCRIPT_PID}
  clean_up 1
fi
sleep 2
