import React from 'react';
import HeaderComponent from 'components/Header/HeaderComponent.jsx';
import SubscribeComponent from 'components/Subscribe/SubscribeComponent.jsx';

export default class IndexComponent extends React.Component {
  render() {
    return (
      <section className="container">
        <HeaderComponent />
        <section>
          {this.props.items.map((item, index) => {
            return <div className="textbox medium">{item}</div>
          })}
        </section>
        <SubscribeComponent />
      </section>
    );
  }
}

IndexComponent.defaultProps = {
  items: []
};
