// frontend/src/components/LoginFormModal/LoginFormModal.jsx
import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };
  // const handleLoginDemoUser = (e) => {
  //   e.preventDefault();
  //   const demoUserEmail = 'demo@user.io';
  //   const demoUserPassword = 'password';
  //   return dispatch(sessionActions.login({ credential:demoUserEmail, password: demoUserPassword }))
  //     .then(closeModal)
  //     .catch(async (res) => {
  //       const data = await res.json();
  //       if (data?.message) {
  //         setErrors({credential: 'There was an error with demo user login'});
  //       }
  //     });
  //
  // };

  // Check if the login button should be disabled
  const isButtonDisabled = email.length < 4 || password.length < 6;

  return (
    <div className="modal-box" data-testid="login-modal">
      <h1 className="login-title">Log In</h1>
      {errors && (
        <p className="error-message-login">{errors.credential}</p>
      )}
      <form onSubmit={handleSubmit} className="login-form">
        <label className="form-label">
          Email
        </label>
        <input
          data-testid="credential-input"
          type="text"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className="input-field"
        />
        {errors.email && <p className="error-message-login">{errors.email}</p>}

        <label className="form-label">
          Password
        </label>
        <input
          data-testid="password-input"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          className="input-field"
        />{errors.password && <p className="error-message-login">{errors.password}</p>}

        <button
          data-testid="login-button"
          type="submit"
          className="login-button"
          disabled={isButtonDisabled}
        >
          Log In
        </button>
      </form>
      {/*<button className="demo-user-login" data-testid={'demo-user-login'} onClick={handleLoginDemoUser}>Login in demo user</button>*/}
    </div>
  );
}

export default LoginFormModal;
