import { useAuth } from "../../context/AuthContext";
import "../../styles/dashboard.css";

export default function MainDashboardPage() {
  const { user } = useAuth();

  return (
    <div className="dash-page">
      <div className="dash-shell">
        {/* Sidebar */}
        <aside className="dash-sidebar">
          <div className="brand">
            <div className="brand-dot" />
            <h2>SecureRide</h2>
          </div>

          <div className="driver-card">
            <p className="muted">Driver</p>
            <h3>{user?.fullNames || "Driver Name"}</h3>
            <span className="tag">{user?.accountType || "driver"}</span>
          </div>

          <nav className="dash-nav">
            <button className="nav-item active">Dashboard</button>
            <button className="nav-item">Trips</button>
            <button className="nav-item">Earnings</button>
            <button className="nav-item">Documents</button>
            <button className="nav-item">Support</button>
          </nav>

          <div className="sidebar-footer">
            <button className="nav-item">Settings</button>
          </div>
        </aside>

        {/* Content */}
        <main className="dash-main">
          <header className="dash-header">
            <h1>Dashboard</h1>
            <button className="online-btn">Go Online</button>
          </header>

          {/* Top stats */}
          <section className="stats-grid">
            <article className="stat-card highlight">
              <p>Today’s Earnings</p>
              <h2>R 1,240</h2>
              <small>+12% from yesterday</small>
            </article>

            <article className="stat-card">
              <p>Trips Completed</p>
              <h2>18</h2>
              <small>4 pending requests</small>
            </article>

            <article className="stat-card">
              <p>Driver Rating</p>
              <h2>4.92 ★</h2>
              <small>Based on 326 reviews</small>
            </article>
          </section>

          {/* Main widgets */}
          <section className="widgets-grid">
            <article className="panel large">
              <div className="panel-head">
                <h3>Weekly Trips</h3>
                <span className="pill">7 days</span>
              </div>
              <div className="bars">
                {[40, 62, 35, 70, 55, 82, 66].map((h, i) => (
                  <div key={i} className="bar-wrap">
                    <div className="bar" style={{ height: `${h}%` }} />
                  </div>
                ))}
              </div>
            </article>

            <article className="panel side">
              <h3>Verification Status</h3>
              <ul className="check-list">
                <li>{user?.carDetailsCompleted ? "✅" : "❌"} Car details</li>
                <li>{user?.idDocumentUploaded ? "✅" : "❌"} ID uploaded</li>
                <li>{user?.faceVerified ? "✅" : "⏭️"} Face verification</li>
              </ul>
            </article>

            <article className="panel">
              <h3>Recent Activity</h3>
              <p>• Trip to Sandton — R145</p>
              <p>• Trip to Midrand — R98</p>
              <p>• Trip to Pretoria CBD — R210</p>
            </article>

            <article className="panel map-card">
              <h3>Service Area</h3>
              <div className="fake-map">
                <div className="pulse one" />
                <div className="pulse two" />
                <div className="pulse three" />
              </div>
            </article>
          </section>
        </main>
      </div>
    </div>
  );
}