import { Link } from "react-router-dom";
import "../../styles/auth.css";

export default function RegisterPage() {
  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-left">
          <div className="watermark">SR</div>
          <div className="brand-content">
            <h2>SecureRide</h2>
            <p>
              Create your verified account using your official personal details.
            </p>
          </div>
          <div className="left-footer">
            <span>About</span>
            <span>FAQ</span>
            <span>Support</span>
          </div>
        </div>

        <div className="auth-right">
          <h1>Create Account</h1>
          <p className="subtitle">Fill in your details to register.</p>

          <form className="auth-form">
            <div className="field">
              <label>Full Names (as per ID)</label>
              <input type="text" placeholder="e.g. Vhugala Mathivha" />
            </div>

            <div className="field">
              <label>ID Number</label>
              <input type="text" placeholder="South African ID Number" />
            </div>

            <div className="field">
              <label>Gender</label>
              <select>
                <option value="">Select gender</option>
                <option value="female">Female</option>
                <option value="male">Male</option>
                <option value="other">Other</option>
                <option value="prefer_not_to_say">Prefer not to say</option>
              </select>
            </div>

            <div className="field">
              <label>Race</label>
              <select>
                <option value="">Select race</option>
                <option value="african">African</option>
                <option value="coloured">Coloured</option>
                <option value="indian_asian">Indian / Asian</option>
                <option value="white">White</option>
                <option value="other">Other</option>
                <option value="prefer_not_to_say">Prefer not to say</option>
              </select>
            </div>

            <div className="field">
              <label>Account Type</label>
              <select>
                <option value="">Select account type</option>
                <option value="driver">Driver</option>
                <option value="passenger">Passenger</option>
              </select>
            </div>

            <div className="field">
              <label>Address</label>
              <input type="text" placeholder="Street, suburb, city, postal code" />
            </div>

            <div className="field">
              <label>Email Address</label>
              <input type="email" placeholder="you@example.com" />
            </div>

            <div className="field">
              <label>Contact Number</label>
              <input type="tel" placeholder="+27..." />
            </div>

            <div className="field">
              <label>Create Password</label>
              <input type="password" placeholder="••••••••" />
            </div>

            <div className="field">
              <label>Confirm Password</label>
              <input type="password" placeholder="••••••••" />
            </div>

            <button type="submit" className="btn-primary">
              Register
            </button>
          </form>

          <p className="switch-auth">
            Already have an account?{" "}
            <Link to="/login" className="auth-link">
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}