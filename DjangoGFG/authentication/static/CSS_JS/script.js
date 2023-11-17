const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () =>
    container.classList.add('right-panel-active'));

signInButton.addEventListener('click', () =>
    container.classList.remove('right-panel-active'));



    function validatePassword() {
        // Get the entered password
        var password = document.getElementById('password').value;
    
        // Perform manual password validation
        if (!isPasswordValid(password)) {
            // Display an error message
            alert('Password must be at least 8 characters long and contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special symbol.');
            return false;  // Prevent form submission
        }
    
        return true;  // Allow form submission
    }
    
    function isPasswordValid(password) {
        // Define your password complexity requirements
        var lengthRegex = /.{8,}/;
        var uppercaseRegex = /[A-Z]/;
        var lowercaseRegex = /[a-z]/;
        var digitRegex = /\d/;
        var symbolRegex = /[\W_]/; // Matches any non-alphanumeric character
    
        // Check if the password meets all requirements
        return lengthRegex.test(password) &&
            uppercaseRegex.test(password) &&
            lowercaseRegex.test(password) &&
            digitRegex.test(password) &&
            symbolRegex.test(password);
    }