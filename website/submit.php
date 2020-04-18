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
    shell_exec("python3 /stuff/form_data.py $_POST[name] $_POST[email] $_POST[phone] ");
?>
