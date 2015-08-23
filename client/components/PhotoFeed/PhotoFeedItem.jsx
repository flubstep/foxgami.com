import React from 'react';
import timeago from 'timeago';
import {Link} from 'react-router';

export default React.createClass({

  render() {
    var story_date = new Date(this.props.item.submitted_at);
    var story_timeago = timeago(story_date);
    return (
    	<section className='item story-photo'>
        <Link to="item" params={{storyId: this.props.item.id}}>
            <img src={this.props.item.image_url} />
        </Link>
        <p className="textbox medium">{this.props.item.title}</p>
        <p className="x-small">posted {story_timeago}</p>
    	</section>
    );
  }
});