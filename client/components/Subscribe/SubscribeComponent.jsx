import React from 'react';

export default class SubscribeComponent extends React.Component {
  render() {
    return (
      <section className="subscribe">
        <input placeholder="Your e-mail" className="medium" name="subscribeEmail"></input>
        <div className="button large flex-centered-xy">SUBSCRIBE</div>
      </section>
    );
  }
}