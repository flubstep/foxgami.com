import React from 'react';
import StoryPhotoComponent from 'components/StoryPhoto/StoryPhotoComponent.jsx';
import BackButtonComponent from 'components/BackButton/BackButtonComponent.jsx';
import foxgamiApi from 'helpers/foxgamiApi.jsx';

export default React.createClass({

  getInitialState() {
    return { item: null, comments: [] };
  },

  componentDidMount() {
    foxgamiApi.get('/stories/' + this.props.params.storyId).then((story) => {
      this.setState({ item: story.data, comments: story.linked });
    });
  },

  render() {
    if (this.state.item) {
      return (
        <section className="story-photo outer">
          <BackButtonComponent />
          <StoryPhotoComponent item={this.state.item} comments={this.state.comments} />
        </section>
      );
    } else {
      return (
        <section className="story-photo outer"></section>
      );
    }
  }

})