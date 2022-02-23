const emailInput = document.getElementById('email-input');
const submitBtn = document.getElementById('submit-btn');
const form = document.getElementById('form');

const host = `http://localhost:8080/api`;
// const host = window.location.protocol + window.location.host;

let isValid = false;


/*
* When the window loads, we set the focus on the input
* field right away for user convenience.
*
* The input field will initially always be 'invalid', simply
* because there is no input yet, so we call handleDisabledState.
**/
window.onload = () => {
    emailInput.focus();
    handleDisabledState();
    console.log(host)
}

submitForm = ( e ) => {
    const email = emailInput.value;
    // prevent the browser from reloading page on submit
    e.preventDefault();
    // post request to specified endpoint and data we want to send
    post( "/email", { email } );
};

/**
 * Whenever the form is *not* valid, we let the user know by
 * painting the border-bottom-color red ♫ and present a visual
 * cue that the button cannot be clicked ( we do this by adding
 * the CSS class 'disabled', of which the properties are defined
 * in the css file styles/components/button.css ).
 *
 * When isValid is true, we remove that disabled class and reset
 * the bottom border color to the initial colour ( which is also
 * defined in the same CSS file ).
 */
handleDisabledState = () => {
    if ( isValid ){
        submitBtn.classList.remove('disabled');
        emailInput.style.borderBottomColor = 'initial';
    } else {
        submitBtn.classList.add('disabled');
        emailInput.style.borderBottomColor = 'red';
    }
};

formIsValid = () => {
    // isValid becomes true when the length of the email field value
    // is not 0
    isValid = emailInput.value.length !== 0;

    // isValid may have changed values now, so we handle the same
    // disabled states as before accordingly
    handleDisabledState();
};

/**
 * Post request with the url ( the endpoint ) to send it to, and the
 * data we want to send
 *
 * @param { string } url
 * @param { Object } data
 */
post = ( url, data ) => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `${host}${url}` );

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            alert(xhr.responseText);
        }};

    xhr.send( JSON.stringify(data) );
};

// Event listeners
form.addEventListener('submit', submitForm );
emailInput.addEventListener('keyup', formIsValid );
