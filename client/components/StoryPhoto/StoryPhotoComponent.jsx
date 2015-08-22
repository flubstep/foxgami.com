import React from 'react';
import ShareButtonsComponent from 'components/ShareButtons/ShareButtonsComponent.jsx';
import CommentsFeedComponent from 'components/CommentsFeed/CommentsFeedComponent.jsx';

export default React.createClass({

  render() {
    return (
      <section>
        <img src={this.props.item.image_url} />
        <div className="padding-16 story-section">
          <p className="medium">{this.props.item.title}</p>
          <p className="small">posted 5 hours ago</p>
          <ShareButtonsComponent />
          <div className="horizontal-rule"></div>
        </div>
        <CommentsFeedComponent comments={this.props.comments} />
      </section>
    );
  }

})