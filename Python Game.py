<html>
<head>
	<title>Guess the Number</title>
	<script>
		var number = Math.floor(Math.random() * 100) + 1;
		var guesses = 0;
		
		function checkGuess() {
			var userGuess = document.getElementById("guess").value;
			guesses++;
			
			if(userGuess == number) {
				alert("Congratulations! You guessed the number in " + guesses + " guesses!");
			}
			else if(userGuess < number) {
				alert("Too low! Guess again.");
			}
			else {
				alert("Too high! Guess again.");
			}
		}
	</script>
</head>
<body>
	<h1>Guess the Number</h1>
	<p>I'm thinking of a number between 1 and 100. Can you guess what it is?</p>
	<input type="text" id="guess" />
	<input type="button" value="Guess" onclick="checkGuess()" />
</body>
</html>
