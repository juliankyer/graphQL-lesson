import React, { Component } from 'react';
import './App.css';

import mockData from '../mock-data';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: '',
      names: [],

    };
  }

  handleChange(e) {
    this.setState({ inputValue: e.target.value });
  }

  handleClick(e) {
    e.preventDefault();
    console.log(this.state.inputValue);

    // Grab value from input field
    // pass question to question component
    // make call to DB of names
    // shuffle and divide names into thirds
    // display names in thirds
  }

  render() {
    return (
      <div className="App">
        <h1>comrade questions</h1>
        <input id="question-input" 
               type="text" 
               placeholder="Add new question" 
               value={ this.state.value }
               onChange={ (e) => this.handleChange(e) }
        />
        <button onClick={ (e) => this.handleClick(e) }>Create</button>
      </div>
    );
  }
}

export default App;
