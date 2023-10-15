<?php 
session_start();
if(empty($_SESSION['user'])){
   $_SESSION['user']='2';
}
if (!empty($_SESSION['sqlite_Project2PathDB'])) {
    try{
        $conn =new PDO("sqlite:".        $_SESSION['sqlite_Project2PathDB']);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $_SESSION['sqlite_Project2Connected'] = 1;
    } catch (PDOException $e) {
        echo"<script>alert('Could not connect to the Database')</script>";
    }
}
$_SESSION['PageName']='sqlite_Project2';
if (isset($_REQUEST['PageName'])) {
    $_SESSION["PageName"] = "sqlite_Project2";
    echo'<meta http-equiv="refresh"content="0; URL=Copy.php" />';
}
if(empty($_SESSION['sqlite_Project2Title'])) {
$_SESSION['sqlite_Project2Title'] ='sqlite_Project2';
}
if(empty($_SESSION['sqlite_Project2CurrentPage'])) {
