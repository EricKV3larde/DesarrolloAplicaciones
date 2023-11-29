// Feedback.js
import React, { useState } from 'react';

const Feedback = () => {
  const [feedback, setFeedback] = useState('');

  const handleFeedbackChange = (e) => {
    setFeedback(e.target.value);
  };

  const handleSubmit = () => {
    // Aquí puedes manejar la lógica para enviar el feedback
    console.log('Feedback enviado:', feedback);
    // También podrías hacer una solicitud a un servidor para enviar el feedback
    // Por ejemplo, usando fetch() o axios
  };

  return (
    <div>
      <h2>Feedback Page</h2>
      <p>Envía tus comentarios:</p>
      <textarea value={feedback} onChange={handleFeedbackChange} rows={4} cols={50} />
      <br />
      <button onClick={handleSubmit}>Enviar Feedback</button>
    </div>
  );
};

export default Feedback;
