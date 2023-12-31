import React, {useState} from 'react'
import SwitchButtonContainer from '../../components/UI/SwitchButtonContainer'
import SwitchButton from '../../components/UI/SwitchButton'
import NavBarItem from '../../components/UI/NavBarItem'
import MobileTopBar from '../../components/mobile/MobileTopBar'
import MobileBottomBar from '../../components/mobile/MobileBottomBar'

function Search() {
  const SEARCH_TABS = ['For you', 'Trending', 'News', 'Sports', 'Entertaiment']
  const [SelectedTab, setSelectedTab] = useState('For you')
  return (
    <section>
        <MobileTopBar middleSection='search'/>
        <SwitchButtonContainer>
            {SEARCH_TABS.map(tab => {
               return <SwitchButton key={tab} Name={tab} Selected={SelectedTab} setSelectedTab={() => setSelectedTab(tab)}/>
            })}
        </SwitchButtonContainer>
        <ul className='moblie-side-nav-ul'>
            <NavBarItem item={'Trending'} className={'p-2'}/>
            <NavBarItem item={'Trending'} className={'p-2'}/>
            <NavBarItem item={'Trending'} className={'p-2'}/>
            <NavBarItem item={'Trending'} className={'p-2'}/>
            <NavBarItem item={'Trending'} className={'p-2'}/>
            <NavBarItem item={'Trending'} className={'p-2'}/>
        </ul>
    </section>
  )
}

export default Search