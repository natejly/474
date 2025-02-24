#!/bin/bash
# test.sh - Script to verify that ShutTheBox returns the expected outputs and display timing

# Flag to mark if any test fails
fail=0

# Function to run a test case.
# Arguments:
#   $1 - The command to run
#   $2 - The expected output
run_test() {
  cmd="$1"
  expected="$2"
  
  echo "Running: $cmd"
  
  # Record start time in seconds with nanosecond precision.
  start=$(date +%s.%N)
  
  # Capture the output (both stdout and stderr if needed)
  output=$(eval "$cmd" 2>&1)
  
  # Record end time.
  end=$(date +%s.%N)
  
  # Calculate elapsed time using bc for floating point arithmetic.
  elapsed=$(echo "$end - $start" | bc)
  
  # Compare the actual output to the expected output.
  if [ "$output" = "$expected" ]; then
    echo "PASS"
  else
    echo "FAIL"
    echo "  Expected: $expected"
    echo "  Got:      $output"
    fail=1
  fi
  
  # Print the time taken for this test.
  echo "Time taken: ${elapsed}s"
  echo "-----------------------------"
}

# Test cases
run_test "./ShutTheBox --one --expect 123456789" "0.502810"
run_test "./ShutTheBox --one --expect 146789" "0.256254"
run_test "./ShutTheBox --one --move 146789 9" "[9]"
run_test "./ShutTheBox --two --expect 123456789 8" "0.381212"
run_test "./ShutTheBox --two --expect 12345689 41" "1.000000"
run_test "./ShutTheBox --two --expect 13456789 43" "0.986111"
run_test "./ShutTheBox --two --move 13456789 17 12" "[3, 9]"

# Final report
if [ $fail -eq 0 ]; then
  echo "All tests passed."
  exit 0
else
  echo "Some tests failed."
  exit 1
fi
