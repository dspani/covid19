<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<html lang="en">

<head>
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet">
    <link type="text/css" rel="stylesheet" href="style.css">
</head>

<body>
    <div>
        <title>🔔 Covid-19 Updates</title>
        <h1> Sign up for daily updates on COVID-19</h1>
    </div>

    <div>
        <form action="submit.php" method="post">
            <p>Name: </p>
            <input type="text" name="name">
            <p></p>
            <label>
                Country:
            </label>
            <select id="country">
                <option value="us">United States</option>
                <option value="ko">South Korea</option>
            </select>
            <p>Email: </p>
            <input type="text" name="email">
            <p>Phone number: </p>
            <input type="text" name="phone">
            <p></p>
            <input type="radio" id="email" name="type" value="email">
            <label for="email">Email only</label>
            <input type="radio" id="phone" name="type" value="phone">
            <label for="phone">Text only</label>
            <input type="radio" id="both" name="type" value="both">
            <label for="both">Both</label>
            <p>

            </p>
            <input class="button" type="submit" value="Submit">
        </form>
    </div>


</body>

</html>