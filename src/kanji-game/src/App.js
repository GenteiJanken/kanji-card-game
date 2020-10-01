import React, { Component } from 'react';
import './App.css';
import Button from 'react-bootstrap/Button';
import GameScreen from './GameScreen';

class App extends Component {
  render() {
    let buttonText = 'Start';
    return (
      <div className="App">
        <h2 className="game-page-heading">Kanji Card Game</h2>
        <Button className="btn btn-primary game-start-button">
          {buttonText}
        </Button>
        <GameScreen />
      </div>
    );
  }
}

export default App;
