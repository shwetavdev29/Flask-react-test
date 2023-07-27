import React, { useState } from "react";

const Form = () => {
  const [inputText, setInputText] = useState("");
  const [inputNumber, setInputNumber] = useState("");
  const [outputText, setOutputText] = useState([]);
  const [error, setError] = useState("");

  const handleInputChange = (event) => {
    setError("");
    const { name, value } = event.target;
    if (name === "inputText") {
      setInputText(value);
    } else if (name === "inputNumber") {
      setInputNumber(value);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (inputText.trim() === "" || isNaN(inputNumber) || +inputNumber <= 0) {
      setError("Please enter a valid string and a positive number.");
    } else {
      const repeatedText = inputText.repeat(+inputNumber);
      setOutputText(repeatedText);
      setInputText("");
      setInputNumber("");
    }
  };

  return (
    <div>
      <h3>Task 1</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ paddingBottom: "10px" }}>
          <label
            style={{
              fontFamily: "sans-serif",
              fontSize: "20px",
              padding: "5px 5px 5px 5px"
            }}
          >
            Enter name:
            <input
              type="text"
              name="inputText"
              value={inputText}
              onChange={handleInputChange}
              style={{
                fontFamily: "sans-serif",
                fontSize: "20px"
              }}
            />
          </label>
        </div>
        <div style={{ paddingBottom: "10px" }}>
          <label
            style={{
              fontFamily: "sans-serif",
              fontSize: "20px",
              padding: "5px 5px 5px 5px"
            }}
          >
            Number of times repeative:
            <input
              type="number"
              name="inputNumber"
              value={inputNumber}
              onChange={handleInputChange}
              style={{
                fontFamily: "sans-serif",
                fontSize: "20px"
              }}
            />
          </label>
        </div>
        <button
          type="submit"
          style={{
            fontFamily: "sans-serif",
            fontSize: "20px",
            color: "white",
            backgroundColor: "green",
            borderRadius: "5px",
            borderColor: "green"
          }}
        >
          Submit
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {outputText && <p>{outputText}</p>}
    </div>

  );
};



export default Form;