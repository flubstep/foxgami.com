import React from 'react';

export default class SidePhotoComponent extends React.Component {
  render() {
    return (
      <section className="photo-holder flex-centered-xy">
      	<img className="photo-small" src={this.props.src} />
      </section>
    );
  }
}