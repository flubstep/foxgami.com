import React from 'react';

export default class CenterPhotoComponent extends React.Component {
  render() {
    return (
      <section className="photo-holder flex-centered-xy">
      	<img className="photo" src={this.props.src} />
      </section>
    );
  }
}