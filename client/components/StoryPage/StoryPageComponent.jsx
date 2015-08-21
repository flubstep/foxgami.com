import React from 'react';
import StoryPhotoComponent from 'components/StoryPhoto/StoryPhotoComponent.jsx';

export default React.createClass({

  getInitialState() {
    return {
      item: {
        'title': 'Dog makes a bad ass leap',
        'image_url': '/client/resources/clip1.jpg'
      }
    };
  },

  render() {
    return (
      <section className="story-photo">
        <StoryPhotoComponent item={this.state.item} />
      </section>
    );
  }

})