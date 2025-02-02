import 'bootstrap/dist/css/bootstrap.min.css';
import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className="mx-3 mt-3">
      <h1 className="text-center mb-4">Patient Monitoring Dashboard</h1>

      {/* Row 1 */}
      <div className="d-flex flex-column flex-md-row m-3">
        {/* Left Section - Patient Info */}
        <div className="col-md-4 border p-3 me-3" style={{ borderColor: '#d3d3d3' }}>
          <h4>Patient Info</h4>
          <div className="d-flex flex-column flex-md-row align-items-start">
            <img
              src="/anonymous_patient_image.png"
              alt="Patient Profile"
              className="img-fluid rounded mb-3 mb-md-0"
              style={{ maxWidth: '150px' }}
            />
            <div className="ms-md-3">
              <p>Patient Name: ____________</p>
              <p>Blood Type: ____________</p>
              <p>Date of Birth: ____________</p>
              <p>Pronouns: ____________</p>
            </div>
          </div>

          <div className="d-flex flex-row mt-3">
            <button className="btn btn-secondary me-2">Full Clinical Access</button>
            <button className="btn btn-secondary me-2">Support Staff View</button>
          </div>
        </div>

        {/* Right Section - Heartbeat Tracking */}
        <div className="col-md-8 border p-3" style={{ borderColor: '#d3d3d3' }}>
          <h4>Heartbeat Tracking</h4>
          <div className="d-flex flex-column flex-md-row justify-content-between" style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '5px' }}>
            
            {/* Heart Rate Container */}
            <div className="text-center border p-3 me-md-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
              <h5>Heart Rate</h5>
              <p style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>___ bpm</p>
            </div>

            {/* Average Heart Rate Container */}
            <div className="text-center border p-3 me-md-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
              <h5>Average Heart Rate</h5>
              <p style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>___ bpm</p>
            </div>

            {/* Scanning Status Container */}
            <div className="text-center border p-3" style={{ flex: 1, borderColor: '#d3d3d3', borderRadius: '5px' }}>
              <h5>Status</h5>
              <p style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'green' }}>Scanning</p>
              {/* Change 'Scanning' to 'Not Scanning' and update color to red dynamically */}
            </div>

          </div>
        </div>

      </div>


      {/* Row 2 */}
      <div className="d-flex flex-column flex-md-row m-3">
        {/* Bottom Left - Facial Expression Tracking */}
        <div className="col-md-7 border p-3 me-md-3" style={{ borderColor: '#d3d3d3', height: '400px' }}>
          <h4>Facial Expression Tracking</h4>
          <div style={{ height: '100%', backgroundColor: '#f8f9fa', borderRadius: '5px', overflow: 'hidden', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            {/* Embed the Flask video feed */}
            <img
              src="http://127.0.0.1:5000/video_feed"
              alt="Video Feed"
              style={{ width: '100%', height: 'auto', maxHeight: '100%', objectFit: 'contain', borderRadius: '5px' }}
            />
          </div>
        </div>

        {/* Bottom Right - Speech Pattern Tracking */}
        <div className="col-md-5 border p-3" style={{ borderColor: '#d3d3d3', height: '400px' }}>
          <h4>Speech Pattern Tracking</h4>
          <div style={{ height: '100%', backgroundColor: '#f8f9fa', padding: '10px', overflowY: 'auto' }}>
            <p>01/02/2025 - 20:08:11: Patient talks about trees - neutral</p>
            <p>01/02/2025 - 20:08:12: Patient talks about beach - passive</p>
            <p>01/02/2025 - 20:08:13: Patient reminisces about war - aggressive</p>
            <p>01/02/2025 - 20:08:14: ...</p>
            <p>01/02/2025 - 20:08:15: ...</p>

            <div className="mt-3 text-danger">
              <strong>Danger Alert:</strong> Patient mentioned war, violence, and crimes.
            </div>
          </div>
        </div>
      </div>

    </div>
  );
}
