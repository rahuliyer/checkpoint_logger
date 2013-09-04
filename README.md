checkpoint_logger
=================

checkpoint_logger is a simple checkpoint logger written in python. It writes checkpoints encoded in json into a file.
On startup it can read existing checkpoints and rebuild state. 

Here's an example of how to use it:
# First create an instance of checkpoint_logger. You must pass it a directory. It creates a subdirectory called
# .checkpoint under the directory you provided. This is where it stores the files with the checkpoints.
>>> from checkpoint import Checkpoint
>>> x = Checkpoint("/tmp")

# Next, create a checkpoint log key. A key corresponds to a checkpoint stream. In the current implementation it is a
# file. Writes to a given key are *not* thread safe and external synchronization is expected. Using separate keys, 
# multiple threads can log events without needing synchronization.
>>> x.createCheckpointLog("test_key")

# Write a few checkpoints. The first parameter is the checkpoint log key you created above. The second argument is 
# an object whose state got modified and the third is the mutation itself. In the example below, the object "photo123"
# was first uploaded and then added to an album. The objects and events can be arbitrary strings and are defined by
# the user.
>>> x.writeCheckpoint("test_key", "photo123", "UPLOADED")
>>> x.writeCheckpoint("test_key", "photo123", "ADDED_TO_ALBUM")

# To get the checkpoints for a given object, simply call getCheckpoints()
>>> x.getCheckpoints("photo123")
['UPLOADED', 'ADDED_TO_ALBUM']
