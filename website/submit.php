<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<?PHP
    echo "Name : ";
    echo $_POST[name];
    echo "<br>";
    echo "Email : ";
    echo $_POST[email];
    echo "<br>";
    echo "Phone : ";
    echo $_POST[phone];
    echo "<br>";
    //echo shell_exec("python3 /stuff/hook.py name1 name2 name3");
    echo shell_exec("python3 /stuff/hook.py $_POST[name] $_POST[email] $_POST[phone] ");
?>
