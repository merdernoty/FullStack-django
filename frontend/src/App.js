import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  state = { details: [], error: null };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000")
      .then((res) => {
        this.setState({
          details: res.data,
          error: null,
        });
      })
      .catch((err) => {
        this.setState({
          details: [],
          error: "An error occurred while fetching data.",
        });
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        <header>Data with Django</header>
        <hr></hr>
        {this.state.error ? (
          <p>{this.state.error}</p>
        ) : (
          this.state.details.map((output, id) => (
            <div key={id}>
              <div>
                <h2>{output.title}</h2>
                <p>{output.channel}</p>
              </div>
            </div>
          ))
        )}
      </div>
    );
  }
}

export default App;
