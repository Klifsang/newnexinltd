import React from 'react'
import { Box,IconButton } from '@mui/material'
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import Person2OutlinedIcon from '@mui/icons-material/Person2Outlined';
import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';
import { Link } from 'react-router-dom';
function TopNav({toggleColor,darkTheme}) {
  const ThemeStyles={
    backgroundColor:darkTheme?"rgd(23, 5, 5)":"rgb(84, 35, 13)",
    color:darkTheme?"rgb(13, 13, 13)":"rgb(255 255 255)",
  };
  return (
    

    <Box  className="flex justify-between mt-2 p-5" style={ThemeStyles} >
    {/*searchbar*/}
    <Box className="flex">
      {/* <input className="text-slate-700 bg-sky-950 " placeholder="search"/> */}
      <IconButton style={ThemeStyles} className="text-slate-700">
        
      </IconButton>
      
    </Box>
    {/*icons*/}
    <Box display="flex p-2">
      <IconButton style={ThemeStyles} className="text-xl"  onClick={toggleColor}>
       {darkTheme?<DarkModeOutlinedIcon/>:<LightModeOutlinedIcon />}
      </IconButton>
      
     
      <Link to="/Profile">
        <IconButton className="text-neutral-300" style={ThemeStyles}>
        <Person2OutlinedIcon />
      </IconButton>
      </Link>
      
    </Box>
  </Box>

    
  )
}

export default TopNav