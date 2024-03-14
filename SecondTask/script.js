var ApplicationInformation = {
    Id: '1',
    CreatedDate: '2024-03-14',
    Strategy: 'Strategy1',
    SubjectList: [
        {
            Id: '1',
            SubjectIncome: 70000,
            SubjectRole: 'заемщик',
            RegistrationAddress: {
                Region: 'Новосибирская обл.',
                City: 'Новосибирск',
                House: '1'
            }
        },
        {
            Id: '2',
            SubjectIncome: 50000,
            SubjectRole: 'Role2',
            RegistrationAddress: {
                Region: 'Region2',
                City: 'City2',
                House: '2'
            }
        }
    ]
};


function checkApplication(application) {
    for (var i = 0; i < application.SubjectList.length; i++) {
        var client = application.SubjectList[i];
        if (client.SubjectRole === 'заемщик' && client.RegistrationAddress.Region === 'Новосибирская обл.' && client.SubjectIncome > 60000) {
            return true;
        }
    }
    return false;
}


console.log(checkApplication(ApplicationInformation));
