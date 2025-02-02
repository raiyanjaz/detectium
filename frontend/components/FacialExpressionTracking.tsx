export default function FacialExpressionTracking() {
    return (
      <div className="col-md-7 border p-3 me-md-3" style={{ borderColor: '#d3d3d3', height: '400px' }}>
        <h4>Facial Expression Tracking</h4>
        <div style={{ height: '100%', backgroundColor: '#f8f9fa', borderRadius: '5px', overflow: 'hidden', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <img
            src="http://127.0.0.1:5000/video_feed"
            alt="Video Feed"
            style={{ width: '100%', height: 'auto', maxHeight: '100%', objectFit: 'contain', borderRadius: '5px' }}
          />
        </div>
      </div>
    );
  }
  