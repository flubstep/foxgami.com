import React from 'react';

export default React.createClass({

  render() {
    return (
      <section className='comment-feed padding-16 story-section'>
        <h2 className="medium">Comments ({this.props.comments.length})</h2>
        {this.props.comments.map((comment, index) => {
          if (comment.replies == 0) {
            var commentDiv = '';
          } else if (comment.replies == 1) {
            var commentDiv = <p className='textbox xx-small'>{comment.replies} reply</p>;
          } else {
            var commentDiv = <p className='textbox xx-small'>{comment.replies} replies</p>;
          }
          return <section key={comment.id}>
            <p className='username medium'>{comment.user_name}</p>
            <p className='comment-text medium'>{comment.text}</p>
            {commentDiv}
          </section>
        })}
      </section>
    );
  }
});