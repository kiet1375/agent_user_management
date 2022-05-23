

class Login extends React.Component {

	render() {
		return <div id="formContent">
    <h1>Login</h1>
    <div class="content">
      <div class="input-field">
        <input type="email" name="email" placeholder="Email" autocomplete="nope" />
      </div>
      <div class="input-field">
        <input type="password" name="password" placeholder="Password" autocomplete="new-password" />
      </div>
      <a href="#" class="link">Forgot Your Password?</a>
    </div>
    <div class="action">
      <button>Register</button>
      <button>Sign in</button>
    </div>
  </div>
	}
}

ReactDOM.render(<Login />, document.getElementById('form_post'));


