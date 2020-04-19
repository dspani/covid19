<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<html lang="en">

<head>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet">
</head>

<body>
    <div>
        <title>🔔 Covid-19 Updates</title>
        <h1> Sign up for daily updates on COVID-19</h1>
    </div>
    <div>
        <p>Name: </p>
        <?PHP
        echo "<p class='output'>$_POST[name]</p>";
        ?>
        <p>Email: </p>
        <?PHP
        echo "<p class='output'>$_POST[email]</p>";
        ?>
        <p>Phone: </p>
        <?PHP
        echo "<p class='output'>$_POST[phone]</p>";
        ?>
        <p class="result">
            Result:
            <br />
            <?PHP

            echo shell_exec("python3 /stuff/hook.py '$_POST[name]' '$_POST[email]' '$_POST[phone]' ");
            ?>
        </p>
    </div>
</body>

</html>