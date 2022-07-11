import React from 'react';

const Dashboard = () => {
	return (
		<>
			<div className='d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom'>
				<h3 className='h3'>Hussein's Dashboard</h3>
				<div className='btn-toolbar mb-2 mb-md-0'>
					<div className='btn-group me-2'>
						<button type='button' className='btn btn-sm btn-outline-secondary'>
							Share
						</button>
						<button type='button' className='btn btn-sm btn-outline-secondary'>
							Export
						</button>
					</div>
					<button
						type='button'
						className='btn btn-sm btn-outline-secondary dropdown-toggle'>
						<span data-feather='calendar'></span>
						This week
					</button>
				</div>
			</div>
			<div>
				<h5>More info about user's dashboard</h5>
			</div>
		</>
	);
};

export default Dashboard;
