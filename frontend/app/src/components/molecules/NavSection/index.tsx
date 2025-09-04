import type { NavSectionProps } from '../../../types';
import './index.css'


export default function NavSection({ columns, header, body}:NavSectionProps){

    const bodyClassName = `navbar-body  navbar--cols--${columns}`
    return (
    <div className="navbar-section">
        <div className="navbar-header">
            {header}
        </div>
        <div className={bodyClassName}>
            {body}
        </div>
        {/* <Span className='span-navbar-white-s' value="Deliver to"/> */}
    </div>
  );
};
