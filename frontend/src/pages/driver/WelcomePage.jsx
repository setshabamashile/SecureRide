import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function WelcomePage() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  if (!user) return null;

  const goNext = () => {
    if (user.accountType !== "driver") {
      navigate("/driver/trips");
      return;
    }

    if (!user.carDetailsCompleted) {
      navigate("/driver/car-details");
      return;
    }

    if (!user.faceVerified) {
      navigate("/driver/face-verification");
      return;
    }

    navigate("/driver/trips");
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>Welcome, {user.fullNames} 👋</h1>
      <p>Account Type: <b>{user.accountType}</b></p>
      <p>Car details: {user.carDetailsCompleted ? "✅ Complete" : "❌ Not complete"}</p>
      <p>Facial verification: {user.faceVerified ? "✅ Verified" : "❌ Not verified"}</p>

      <button onClick={goNext} style={{ marginRight: 10 }}>Continue</button>
      <button onClick={logout}>Logout</button>
    </div>
  );
}