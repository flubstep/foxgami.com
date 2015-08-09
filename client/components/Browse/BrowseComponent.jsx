import React from 'react';
import HeaderComponent from 'components/Header/HeaderComponent.jsx';
import CenterPhotoComponent from 'components/CenterPhoto/CenterPhotoComponent.jsx';
import SidePhotoComponent from 'components/SidePhoto/SidePhotoComponent.jsx';

export default class BrowseComponent extends React.Component {
  render() {
    return (
      <section>
        <section className="container-small">
          <HeaderComponent />
        </section>
        <section className="photo-container">
          <section className="photo-carousel flex-centered">
            <SidePhotoComponent src="client/resources/test_photo_left.png" />
            <CenterPhotoComponent src="client/resources/test_photo.png" />
            <SidePhotoComponent src="client/resources/test_photo_right.png" />
          </section>
        </section>
      </section>
    );
  }
}

BrowseComponent.defaultProps = {
  items: []
};
