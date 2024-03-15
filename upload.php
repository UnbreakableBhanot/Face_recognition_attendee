<?php
if(isset($_POST['submit'])){
    $file = $_FILES['file'];
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    $fileSize = $_FILES['file']['size'];
    $fileError = $_FILES['file']['error'];
    $fileType = $_FILES['file']['type'];

    $fileExt = explode('.',$fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('jpg', 'jpeg', 'png', 'jfif');
    if (in_array($fileActualExt, $allowed)){
        if ($fileError === 0 ) {
            if ($fileSize < 1000000) {
                $fileNameNew = uniqid('', true).".".$fileActualExt;
                $new_file_name = "image_" . uniqid() . ".jpg";
                $fileDestination = 'C:\Users\shubh\PycharmProjects\Face\ImageAttendance/'.$new_file_name;
                move_uploaded_file($fileTmpName, $fileDestination);
                header("Location: index.php?uploadsuccess");
            } else {
                echo "your file size is large";
            }
        } else {
            echo "there was an error uploading your file";
        }
    }else{
        echo "you cannot upload file of this type";
    }
}
if(isset($_POST['submit_1'])){
    $file = $_FILES['file_1'];
    $fileName = $_FILES['file_1']['name'];
    $fileTmpName = $_FILES['file_1']['tmp_name'];
    $fileSize = $_FILES['file_1']['size'];
    $fileError = $_FILES['file_1']['error'];
    $fileType = $_FILES['file_1']['type'];

    $fileExt = explode('.',$fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('jpg', 'jpeg', 'png', 'jfif');
    if (in_array($fileActualExt, $allowed)){
        if ($fileError === 0 ) {
            if ($fileSize < 5000000) {
                $fileDestination = 'C:\Users\shubh\PycharmProjects\Face\ImagesBasic\img.jpg';
                move_uploaded_file($fileTmpName, $fileDestination);
                header("Location: index.php?uploadsuccess");
            } else {
                echo "your file size is large";
            }
        } else {
            echo "there was an error uploading your file";
        }
    }else{
        echo "you cannot upload file of this type";
    }
}