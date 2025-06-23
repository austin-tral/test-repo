def main():
  # This function contains the code we want to run.
  print("Hello, World!")

# This conditional checks if the script is being run directly.
# If it is, the special variable __name__ will be "__main__".
# If the script is imported, __name__ will be the name of the file.
if __name__ == "__main__":
  main()
