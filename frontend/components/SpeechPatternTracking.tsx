export default function SpeechPatternTracking() {
    return (
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
    );
  }
  