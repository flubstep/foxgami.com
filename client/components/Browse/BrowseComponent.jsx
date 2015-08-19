import React from 'react';
import Draggable from 'react-draggable';
import HeaderComponent from 'components/Header/HeaderComponent.jsx';
import PhotoFeedComponent from 'components/PhotoFeed/PhotoFeedComponent.jsx';

export default class BrowseComponent extends React.Component {
  render() {
    return (
      <section>
        <section className="container-small">
          <HeaderComponent />
        </section>
        <PhotoFeedComponent />
      </section>
    );
  }
}

BrowseComponent.defaultProps = {
  items: []
};
