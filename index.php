<!DOCTYPE html>
<html>
  <head>
    <title>Upload Image to Folder</title>
  </head>
  <body>
    <h1>Upload Attendees Image to below Folder</h1>
    <form action="upload.php" method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <button type="submit" name="submit">Upload Attendee</button>
    </form>
    <h1>Upload group picture to below Folder</h1>
    <form action="upload.php" method="POST" enctype="multipart/form-data">
      <input type="file" name="file_1">
      <button type="submit_1" name="submit_1">Upload Grp. pic</button>
    </form><hr>
    <h1>execute program -<h1>
    <form action="execute.php" method="POST" >
      <button type="submit_2" name="submit_2">Run</button>
    </form>
    <h1>Reset sql</h1>
    <form action="resetSql.php" method="POST" >
      <button type="submit_3" name="submit_3">reset</button>
    </form>
  </body>
</html>
