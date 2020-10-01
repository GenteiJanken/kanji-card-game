import React, { Component } from 'react';
import './App.css';

class GameScreen extends Component {
  render() {
    let challengeKanji = ['日', '一', '人'];
    let propertyHeadings = ['Strokes', 'Kun-yomi', 'On-yomi'];
    let headingElements = propertyHeadings.map((p, i) => (
      <span
        key={'heading ' + i}
        className="property-heading"
        style={{ left: (25 + 25 * i).toString() + '%', top: '7.5%' }}
      >
        {p}
      </span>
    ));
    let cardSlotArray = [];
    for (let i = 0; i < 3; i++) {
      let row = [];
      for (let j = 0; j < 3; j++) {
        row.push(0);
      }
      cardSlotArray.push(row);
    }
    let cardSlotElements = cardSlotArray.map((row, i) =>
      row.map((_, j) => (
        <div
          key={'slot-' + i + '-' + j}
          className="card-slot"
          style={{
            left: (25 + 25 * i).toString() + '%',
            top: (15 + 25 * j).toString() + '%',
          }}
        ></div>
      )),
    );

    let kanjiElements = challengeKanji.map((el, i) => (
      <div
        key={'kanji-' + i}
        className="challenge-kanji"
        style={{ left: '2%', top: (15 + 25 * i).toString() + '%' }}
      >
        {el}
      </div>
    ));

    return (
      <div className="GameScreen">
        {headingElements}
        {cardSlotElements}
        {kanjiElements}
      </div>
    );
  }
}

export default GameScreen;
