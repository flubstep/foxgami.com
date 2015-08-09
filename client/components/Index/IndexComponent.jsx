import React from 'react';
import HeaderComponent from 'components/Header/HeaderComponent.jsx';

export default class IndexComponent extends React.Component {
  render() {
    return (
      <section>
        <HeaderComponent />
        {this.props.items.map((item, index) => {
          return <div className="textbox">{item}</div>
        })}
      </section>
    );
  }
}

IndexComponent.defaultProps = {
  items: []
};
