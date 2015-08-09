import React from 'react';

export default class HeaderComponent extends React.Component {
  render() {
    return (
      <section className="header">
        <div className="flex-centered">
          <img className="logo" src="client/resources/logo_large.png"></img>
        </div>
        <h1>FOXGAMI</h1>
      </section>
    );
  }
}