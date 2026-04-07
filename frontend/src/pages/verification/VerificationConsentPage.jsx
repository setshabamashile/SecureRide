import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../../styles/auth.css";
import ProgressStepper from "../../components/ProgressStepper";

// inside return:
<ProgressStepper currentStep={2} />

export default function VerificationConsentPage() {
  const navigate = useNavigate();
  const [agreed, setAgreed] = useState(false);

  const handleContinue = () => {
    if (!agreed) {
      alert("Please tick the consent checkbox before proceeding.");
      return;
    }
    navigate("/driver/upload-id");
  };

  return (
    <div className="auth-page">
      <div className="auth-card" style={{ gridTemplateColumns: "1fr" }}>
        <div className="auth-right" style={{ padding: "28px" }}>
          <h1>Life Verification Consent</h1>
          <p className="subtitle">
            Please read carefully before continuing.
          </p>

          <div className="consent-box">
            <p><strong>Please read the following carefully before proceeding with the Life Verification process.</strong></p>

            <p>
              By clicking "I Agree" and proceeding with the Life Verification feature within the
              SecureRide application, you (the "User") acknowledge, understand, and provide express
              consent to the following terms regarding the collection and use of your personal and biometric data.
            </p>

            <p><strong>1. Accuracy and Truthfulness of Information</strong><br />
              You declare that all information, documentation, and biometric data provided are true,
              accurate, current, and complete. False or misleading information may result in immediate account termination.
            </p>

            <p><strong>2. Purpose of Data Collection (Safety and Security)</strong><br />
              SecureRide uses life verification to enhance safety in the e-hailing industry by protecting
              drivers and passengers from identity theft, fraud, and harm.
            </p>

            <p><strong>3. Acknowledgment of Liability and Legal Use</strong><br />
              You acknowledge that verified information may form part of a digital audit trail and may be
              used in legal proceedings or shared with authorized law enforcement where required by law.
            </p>

            <p><strong>4. Consent to Processing</strong><br />
              You consent to secure transmission and storage of your verification data in SecureRide systems,
              recognizing inherent risks of digital transmission.
            </p>

            <p><strong>User Declaration:</strong><br />
              "I have read, understood, and voluntarily agree to this Life Verification Consent.
              I certify that I am the person depicted in the provided identification and that all submitted
              information is truthful. I accept responsibility for actions taken through this account."
            </p>
          </div>

          <label className="consent-check">
            <input
              type="checkbox"
              checked={agreed}
              onChange={(e) => setAgreed(e.target.checked)}
            />
            <span>I Agree to the Life Verification Consent</span>
          </label>

          <button className="btn-primary" onClick={handleContinue}>
            Continue to ID Upload
          </button>
        </div>
      </div>
    </div>
  );
}