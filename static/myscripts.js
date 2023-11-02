const passwordField = document.getElementById('password');
const confirmPasswordField = document.getElementById('confirmPassword');
const requirements = document.getElementById('password-requirements').querySelectorAll('p');
const submitButton = document.getElementById('submit-button');
const errorMessage = document.getElementById('error-message');

function validatePassword() {
    const password = passwordField.value;
    const confirmPassword = confirmPasswordField.value;

    // Check password length
    if (password.length >= 8) {
        setRequirementStatus(0, true);
    } else {
        setRequirementStatus(0, false);
    }

    if (/[a-z]/.test(password)) {
        setRequirementStatus(1, true);
    } else {
        setRequirementStatus(1, false);
    }

    if (/[A-Z]/.test(password)) {
        setRequirementStatus(2, true);
    } else {
        setRequirementStatus(2, false);
    }

    if (/[!@#$%^&*()_+{}\[\]:;<>,.?~\\]/.test(password)) {
        setRequirementStatus(3, true);

    } else {
        setRequirementStatus(3, false);
    }

    // Check if passwords match
    if (password === confirmPassword && confirmPassword.length > 0) {
        confirmPasswordField.classList.remove('is-invalid');
        confirmPasswordField.classList.add('is-valid');
    } else {
        confirmPasswordField.classList.remove('is-valid');
        confirmPasswordField.classList.add('is-invalid');
    }

    updateSubmitButtonState();
}

function setRequirementStatus(index, isValid) {
    requirements[index].classList.remove(isValid ? 'invalid' : 'valid');
    requirements[index].classList.add(isValid ? 'valid' : 'invalid');
}

function updateSubmitButtonState() {
    if (Array.from(requirements).every(p => p.classList.contains('valid')) && passwordField.value === confirmPasswordField.value) {
        submitButton.disabled = false;
        errorMessage.style.display = 'none'; // Hide the error message
    } else {
        submitButton.disabled = true;
        submitButton.style.backgroundColor = "red";
        errorMessage.style.display = 'block'; // Show the error message
    }
}

function validateForm() {
    if (!submitButton.disabled) {
        // Form is valid, you can submit it.
        return true;
    } else {
        // Form is not valid, prevent submission.
        errorMessage.style.display = 'block'; // Show the error message
        return false;
    }
}
